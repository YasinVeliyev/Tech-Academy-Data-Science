use std::io::stdin;

fn main() {
    let mut n = String::new();
    let mut k = String::new();
    stdin().read_line(&mut n).unwrap();
    stdin().read_line(&mut k).unwrap();
    let n = n.trim().parse::<u16>().expect("Rəqəm daxil edin");
    let k = k.trim().parse::<u16>().expect("Rəqəm daxil edin");
    println!("{}", k % n);
}
