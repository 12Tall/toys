const { spawn } = require("child_process");

let proc = spawn('./a.out', { stdio: 'pipe' });


proc.stdout.on('data', data => {
    console.log(`stdout: \n ${data} \n`)
});

proc.stderr.on('data', data => {
    console.log(`stdout: \n ${data} \n`)
});

proc.stdin.write('1 9\n');

proc.stdin.write('2 9\n');
