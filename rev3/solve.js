// const o = [
//   9, 31, 119, 94, 183, 0, 33, 34, 175, 123, 129, 19, 5, 7, 235, 55, 16, 50, 171,
//   6, 189, 135, 9, 12, 27, 233, 11, 111, 130, 136, 242, 184, 223, 127, 4, 4, 163,
//   157, 115, 148, 82, 236, 1, 64, 137, 222, 111, 104,
// ];

const o = [
  9, 31, 5, 12, 4, 64, 137, 222, 111, 104, 119, 94, 183, 0, 33, 34, 175, 123,
  129, 19, 7, 235, 55, 16, 50, 171, 6, 189, 135, 9, 27, 233, 11, 111, 130, 136,
  242, 184, 223, 127, 4, 163, 157, 115, 148, 82, 236, 1,
];

const b =
  "RazorPower Co.\nResources\nNotifications\nUsers\nTeams\nScoreboard\nChallenges\nAdmin\nTeam\nProfile\nSettings";

function sus(n) {
  // var b = document.body.innerText.substring(0, 100);
  g = ((g - 1 + b.charCodeAt(p.length % 100) * Math.sqrt(15) + n) % 1) + 1;
  p.push(g);

  if (p.length == 48) {
    check();
  }
}

function hmm(n) {
  var t = 1;
  var f = 2;
  var a = 0;
  for (var i = 0; i < 8; i += 1) {
    a <<= 1;
    if (t + 1 / f <= n) {
      a += 1;
      t += 1 / f;
    }
    f *= 2;
  }
  return a;
}

// document.addEventListener("keydown", (event) => {
//   sus(event.key.charCodeAt(0) / 256);
// });
//
//
let flag = "";

function bruteForceO() {
  let pe = [];
  let g = 1;
  console.log(o.length);
  for (const index in o) {
    const oval = o[index];

    loop: for (let i = 0; i < 256; i++) {
      const val = i / 256;

      g1 =
        ((g - 1 + b.charCodeAt(pe.length % 100) * Math.sqrt(15) + val) % 1) + 1;

      h1 = hmm(g1);
      if (h1 == oval) {
        g = g1;
        pe.push(g1);
        const char = String.fromCharCode(i);
        console.log("found", i, char, "for", oval, val, g1, h1);
        flag += char;
        break loop;
      }
    }
  }
}

bruteForceO();

console.log(flag);
