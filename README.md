### PiMotionDetector

Raspberry Pi powered motion detector with discord bot integration

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
