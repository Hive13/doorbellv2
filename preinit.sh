#!/bin/bash
amixer set PCM unmute
amixer set PCM 100%

aplay ready.wav
