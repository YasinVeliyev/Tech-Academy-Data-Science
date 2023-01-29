use std::io::stdin;

fn print(start_and_end: &str, count: u32) {
    print!("{} ", start_and_end);
    for i in 0..count - 2 {
        print!("- ");
    }
    println!("{}", start_and_end);
}

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n);
    let n: u32 = n.trim().parse().expect("Rəqəm daxil edin");
    print("+", n);
    for i in 0..n - 2 {
        print("+", n);
    }
    print("+", n);
}
