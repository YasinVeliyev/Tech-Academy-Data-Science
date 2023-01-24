use std::io::stdin;

fn main() {
    let mut interval = String::new();
    stdin().read_line(&mut interval).unwrap();
    let k = interval.trim().split(" ").filter(|c|!c.is_empty()).collect::<Vec<&str>>();
    let  start=k[0].trim().parse::<u128>().expect("");
    let  end=k[1].trim().parse::<u128>().expect("");
    println!("{:?}", (start+end)*(end-start+1)/2);
}
