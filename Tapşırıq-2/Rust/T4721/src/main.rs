use std::io::stdin;

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let mut number: u32 = number.trim().parse().expect("Rəqəm daxil edin");
    let mut count = 0;
    while number > 0 {
        if number % 10 == 5 {
            count += 1;
        }
        number /= 10;
    }

    println!("{}", count);
}
