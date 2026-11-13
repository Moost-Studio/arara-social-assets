import React from 'react';
import { Composition } from 'remotion';
import { R01 } from './reels/R01';
import { R01v2 } from './reels/R01v2';
import { R01Props } from './schema';
import { TesteTransicoes } from './reels/TesteTransicoes';
import { FPS } from './lib/tokens';

export const Root: React.FC = () => (
  <>
    <Composition id="R01" component={R01} durationInFrames={450} fps={FPS} width={1080} height={1920} schema={R01Props} defaultProps={R01Props.parse({})} />
    <Composition id="R01v2" component={R01v2} durationInFrames={450} fps={FPS} width={1080} height={1920} schema={R01Props} defaultProps={R01Props.parse({})} />
    <Composition id="TesteTransicoes" component={TesteTransicoes} durationInFrames={102} fps={FPS} width={1080} height={1920} />
  </>
);
