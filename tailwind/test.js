// Smoke tests for pequod-tailwind. Uses Node's built-in test runner.
// Run with: node --test test.js

const test = require("node:test");
const assert = require("node:assert/strict");

const pkg = require("./index.js");

test("log scale has twelve steps from 50 to 950", () => {
  const keys = Object.keys(pkg.log);
  assert.equal(keys.length, 12);
  assert.equal(keys[0], "50");
  assert.equal(keys[keys.length - 1], "950");
});

test("every log value is a six-digit hex code", () => {
  for (const v of Object.values(pkg.log)) {
    assert.match(v, /^#[0-9A-F]{6}$/);
  }
});

test("crew has eight named members with DEFAULT, light, dark", () => {
  const expected = [
    "ahab", "starbuck", "queequeg", "pip",
    "ishmael", "stubb", "tashtego", "daggoo",
  ];
  assert.deepEqual(Object.keys(pkg.crew), expected);
  for (const name of expected) {
    const v = pkg.crew[name];
    assert.match(v.DEFAULT, /^#[0-9A-F]{6}$/);
    assert.match(v.light,   /^#[0-9A-F]{6}$/);
    assert.match(v.dark,    /^#[0-9A-F]{6}$/);
    assert.equal(v.DEFAULT, v.light, "DEFAULT should mirror the light variant");
  }
});

test("colors merges log + crew without aliasing", () => {
  assert.equal(pkg.colors.log, pkg.log);
  assert.equal(pkg.colors.ahab, pkg.crew.ahab);
});

test("known palette exports are frozen", () => {
  assert.equal(Object.isFrozen(pkg.log), true);
  assert.equal(Object.isFrozen(pkg.crew), true);
  assert.equal(Object.isFrozen(pkg.crew.ahab), true);
  assert.equal(Object.isFrozen(pkg.colors), true);
});

test("specific anchor values match the canonical pequod.json", () => {
  assert.equal(pkg.log[50],  "#FBFAF5");
  assert.equal(pkg.log[100], "#F8F4EB");
  assert.equal(pkg.log[800], "#2C3E50");
  assert.equal(pkg.log[950], "#13181F");
  assert.equal(pkg.crew.ahab.light, "#B5534A");
  assert.equal(pkg.crew.starbuck.dark, "#7FA8C3");
});
