use std::io::stdin;

fn main() {
    let mut hotel=String::new();
    stdin().read_line(&mut hotel);
    let k = hotel.trim().split(" ").map(|v|v.parse::<u64>().unwrap()).collect::<Vec<u64>>();
    println!("{} {}",k[0]/k[1],k[0]%k[1]);
}
