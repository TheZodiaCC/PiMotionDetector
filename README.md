### PiMotionDetector

Raspberry Pi powered motion detector (PIR HC-SR501) with discord bot integration

---

1. Configure Discord Bot / Webhook `DiscordConfig` in `config.py`.
2. Configure Motion Detectors in `DetectorsConfig` in `config.py`.
3. Setup Docker container:
   1. Build image: 
   ```
   sudo docker build -t pimotiondetector .
   ```
   2. Run container:
   ```
   sudo docker run --privileged -d \
    -v <path_to_data_dir_on_rpi>:/PiMotionDetector/logs \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    --name pimotiondetector pimotiondetector
   ```
   3. Make container auto startup:
   ```
   sudo docker update --restart unless-stopped pimotiondetector
   ```
   
---

Accessing GPIO from docker container can sometimes not work as expected (especially on RPi Zero ARMV5) in this case use:
1. `python3 -m venv motion_det_venv`
2. `pip3 install -r requirements.txt`
3. `source motion_det_venv/bin/activate`
4. `nohup python3 main.py &`
