# GTAi
## Bot to control GTA V being played on a PS4
The target use case the new Adversary Mode Overtime Shootout.  The bot will be trained to hit a perfect 5 everytime.  This is a trial run for my system, and will be updated for more advanced functionality should this venture be fruitful.
### Flow
- PS4 runs GTA
- PC collects video feed through Remote Play
- OpenCV/Pillow capture screen feed and input that into unverse (8 FPS)
- OpenCV bot determines best move and outputs to DS4 emulator
- Profit

### To test:
- Latency of RP
- DS4 emulation
- Build the damn AI
