use std::io::stdin;

fn main() {
    let mut number = String::new();
    stdin().read_line(&mut number);
    let number = number
        .trim()
        .split(" ")
        .map(|number| number.trim().parse().expect("Rəqəm daxil edin"))
        .collect::<Vec<u32>>();
    'outer: for i in number[0]..=number[1] {
        let mut num = i;
        while num > 0 {
            if num % 10 % 2 == 0 {
                continue 'outer;
            }
            num /= 10;
        }
        print!("{} ", i)
    }
}
