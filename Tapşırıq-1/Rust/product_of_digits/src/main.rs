use std::io::stdin;

fn main() {
    let mut hasil = 1;
    let mut digits = String::new();
    stdin().read_line(&mut digits);
    let mut number = digits.trim().parse::<u64>().expect("Rəqəm daxil edin");
    loop {
        hasil = number % 10 * hasil;
        number /= 10;
        if number == 0 {
            println!("{}", hasil);
            break;
        }
    }
}
