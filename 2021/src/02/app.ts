export function a(input: string[]) {
  let depth = 0;
  let distance = 0;

  input.forEach((line) => {
    const [command, valueString] = line.trim().split(" ");
    const value = Number(valueString);

    switch (command) {
      case "forward":
        distance += value;
        break;
      case "up":
        depth -= value;
        break;
      case "down":
        depth += value;
        break;
      default:
        break;
    }
  });
  return depth * distance;
}

export function b(input: string[]) {
  let depth = 0;
  let distance = 0;
  let aim = 0;

  input.forEach((line) => {
    const [command, valueString] = line.trim().split(" ");
    const value = Number(valueString);

    switch (command) {
      case "forward":
        const depthChange = aim * value;
        depth += depthChange;
        distance += value;
        break;
      case "up":
        aim -= value;
        break;
      case "down":
        aim += value;
        break;
      default:
        break;
    }
  });
  return depth * distance;
}
