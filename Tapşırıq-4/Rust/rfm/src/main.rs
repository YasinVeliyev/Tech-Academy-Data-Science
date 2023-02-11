use polars::lazy::dsl::col;
use polars::prelude::*;
use std::fs::File;
use std::io::{BufRead, BufReader, Cursor, Read};

fn main() -> Result<(), PolarsError> {
    let mut file = File::open("./REKTDATABASE.csv").unwrap();
    let mut data = Vec::new();
    file.read_to_end(&mut data);
    let df = CsvReader::new(Cursor::new(data)).has_header(true).finish();

    println!("{:?}", df);
    Ok(())
}
