use std::io::stdin;

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let mut number: u128 = number.trim().parse().expect("Rəqəm daxil edin");
    let mut reverse = 0;
    while (number > 0) {
        reverse = reverse * 10 + number % 10;
        number /= 10;
    }
    let mut nth = 1;
    let mut odd = 0;
    let mut even = 0;

    while (reverse > 0) {
        if nth % 2 == 1 {
            odd += reverse % 10
        } else {
            even += reverse % 10
        }
        nth += 1;
        reverse /= 10;
    }
    println!("{}", odd * even);
}
