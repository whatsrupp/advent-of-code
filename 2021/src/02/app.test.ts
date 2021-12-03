import { a, b } from "./app";
import fs from "fs";
import path from "path";

it("a", () => {
  const input = fs
    .readFileSync(path.join(__dirname, "/test_input.txt"))
    .toString()
    .split("\n");
  const result = a(input);

  const expected = 150;
  expect(expected).toEqual(result);
});

it("b", () => {
  const input = fs
    .readFileSync(path.join(__dirname, "/test_input.txt"))
    .toString()
    .split("\n");
  const result = b(input);
  const expected = 900;
  expect(expected).toEqual(result);
});
