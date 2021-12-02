export function a(depths: number[]) {
  let increases = 0;

  depths.forEach((depth, i) => {
    const thisDepth = depth;
    const nextDepth = depths[i + 1];

    if (!nextDepth) {
      return;
    }

    if (nextDepth > thisDepth) {
      increases++;
    }
  });

  return increases;
}

export function b(depths: number[]) {
  let increases = 0;

  depths.forEach((depth, i) => {
    const depthA = depth;
    const depthB = depths[i + 1];
    const depthC = depths[i + 2];
    const depthD = depths[i + 3];

    if (!depthD) {
      return;
    }

    const thisRollingWindow = depthA + depthB + depthC;
    const nextRollingWindow = depthB + depthC + depthD;

    if (nextRollingWindow > thisRollingWindow) {
      increases++;
    }
  });

  return increases;
}
