let n;
let k;

process.stdin.on("data", (data) => {
    if (!n) {
        n = parseInt(data);
    } else if (!k) {
        k = parseInt(data);

        process.stdout.write((k % n).toString());
        process.exit();
    } else {
        process.exit();
    }
});
