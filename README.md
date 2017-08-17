# GTAi
## Bot to control GTA V being played on a PS4
### Flow
- PS4 runs GTA
- PC collects video feed through Remote Play
- OpenCV/Pillow capture screen feed and input that into OpenCV-based AI (8 FPS)
- OpenCV bot determines best move and outputs to DS4 emulator
- Profit

### To test:
- Latency of RP
- DS4 emulation
- Build the damn AI
