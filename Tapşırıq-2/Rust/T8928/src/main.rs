use std::io::stdin;

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let number: u128 = number.trim().parse().expect("Rəqəm daxil edin");
    if number % 2 == 0 {
        println!("{}", number / 2)
    } else if number % 3 == 0 {
        println!("{}", number / 3)
    } else {
        let mut greatest_divisior = 1;
        for i in (5..=f64::sqrt(number as f64) as u128).step_by(6) {
            if number % i == 0 {
                greatest_divisior = number / i;
                break;
            } else if number % (i + 2) == 0 {
                greatest_divisior = number / (i + 2);
                break;
            }
        }
        println!("{}", greatest_divisior);
    }
}
