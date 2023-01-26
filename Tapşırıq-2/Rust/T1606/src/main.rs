use std::{io::stdin, num};

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let mut number: i32 = number.trim().parse().expect("Rəqəm daxil edin");
    let mut last = true;
    let mut last_number = 0;
    if number < 0 {
        number *= -1;
    }
    while number >= 10 {
        if last {
            last_number = number % 10;
            last = false;
        }
        number /= 10;
    }
    println!("{}", last_number + number);
}
