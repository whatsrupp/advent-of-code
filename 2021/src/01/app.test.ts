import { a, b } from "./app";
import fs from "fs";
import path from "path";
it("example", () => {
  const expected = 7;

  const input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];

  const result = a(input);

  expect(expected).toEqual(result);
});

it("a", () => {
  const input = fs
    .readFileSync(path.join(__dirname, "/input.txt"))
    .toString()
    .split("\n")
    .map((v) => Number(v));
  const result = a(input);

  const expected = 1529;
  expect(expected).toEqual(result);
});

it("b", () => {
  const input = fs
    .readFileSync(path.join(__dirname, "/input.txt"))
    .toString()
    .split("\n")
    .map((v) => Number(v));
  const result = b(input);

  const expected = 1567;
  expect(result).toEqual(expected);
});
