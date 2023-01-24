use std::io::stdin;

fn main() {
   let mut layers = String::new();
    stdin().read_line(&mut layers);
    let layers = layers.trim().parse::<u64>().unwrap();
    println!("{}",(2*2+(layers-1)*2)*layers/2+1)
}
