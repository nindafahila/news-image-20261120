// Entry for news-image-20261120. The picture itself is entry.png in this
// folder, rendered by draw_entry.py (Python + Pillow) from the verified
// news of Friday 20 November 2026. All this program does is place a copy
// of it at /output/entry.png. The gate accepts one PNG or JPEG, at most
// 1 MiB and 1024x1024; ours is 1024x1024 and about 123 KB, and the copy
// is identical on every run, so the grader sees the same bytes twice.
//
// To try it outside the grader, set MAKEFUN_OUTPUT_DIR instead of /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
const target = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
copyFileSync(source, target);
