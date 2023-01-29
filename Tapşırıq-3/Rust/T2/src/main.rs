use std::io::stdin;

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n);
    match n.trim().parse::<u32>() {
        Ok(n) => {
            for i in 1..=n {
                for j in 0..i {
                    print!("$ ");
                }
                println!("")
            }
        }
        Err(_) => println!("Rəqəm daxil edin"),
    }
}
