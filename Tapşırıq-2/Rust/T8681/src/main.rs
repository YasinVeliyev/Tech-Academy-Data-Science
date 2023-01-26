use std::io::stdin;

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let mut number: u128 = number.trim().parse().expect("Rəqəm daxil edin");
    let mut product = 1;
    while number > 0 {
        let remainder = number % 10;
        if remainder != 0 {
            product *= remainder;
        }
        number /= 10;
    }
    println!("{}", product);
}
