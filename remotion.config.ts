import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('png');
Config.setVideoBitrate('16M');
Config.setPixelFormat('yuv420p');
Config.setOverwriteOutput(true);
Config.setChromiumOpenGlRenderer('swiftshader');
