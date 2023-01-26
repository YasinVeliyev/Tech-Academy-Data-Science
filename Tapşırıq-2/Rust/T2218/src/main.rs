use std::io::stdin;

fn main() {
    let mut count = String::new();
    stdin().read_line(&mut count);
    let mut count: u8 = count.trim().parse().expect("Rəqəm daxil edin");
    let mut zeros = 0;
    let mut ones = 0;
    while count > 0 {
        count -= 1;
        let mut coin = String::new();
        stdin().read_line(&mut coin);
        let coin: u8 = coin.trim().parse().expect("0 və ya 1 daxil edin");
        if coin == 0 {
            zeros += 1
        } else {
            ones += 1
        }
    }

    println!("{}", if ones < zeros { ones } else { zeros })
}
