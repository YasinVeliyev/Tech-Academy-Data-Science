use std::io::stdin;

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n);
    let n: u32 = n.trim().parse().expect("Rəqəm daxil edin");
    for i in 0..n {
        for j in 0..n {
            print!("* ")
        }
        println!("");
    }
}
