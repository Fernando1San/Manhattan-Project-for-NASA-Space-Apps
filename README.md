# Manhattan-Project-for-NASA-Space-Apps
We develop a solution for the 2023 challenge "Managing Fire: Increasing Community-based Fire Management Opportunities".

# General Explanation of the solution
Our solution was divided into two parts: one for communities with internet access and another for those without it.

For communities with internet, the solution involved scraping data from FIRMS to locate potential fires. Once these records are obtained, a message is sent to a Telegram channel with the time and city where the fire is registered. Because our communities primarily speak Spanish, the messages are sent in Spanish to the channel, which is public. However, currently, it is not active due to hosting issues with the code. The bot is capable of recording the time and location where the fire was registered, using Python.

![ejemploTelegram](https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/27ce8861-cf7a-4553-b358-c6518b762529)

For communities without internet, we took a hardware approach. Using a transmission device with an AVR microcontroller family and LoRa communication modules, we were able to send fire alerts from communities with internet access and our alert services to communities lacking these services. Similarly, communities can alert others or nearby cities to request assistance. These devices have a maximum effective range of 10km when placed at heights equal to or greater than 5m, taking into account mountainous areas where transmission/reception areas are reduced.
PCB Designs was created in KiCad an Hardware Prototype in SolidWorks

![esquematico](https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/21d2332a-0637-4f6a-accd-b4089e2feef7)

![PCB1](https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/46e48df2-2b22-4a38-a0fb-e1fe686e3483)
![PCB3](https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/845789d9-e386-4ee0-9001-8b743f5dae1f)
![PCB2](https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/10c868d5-da71-4e39-a896-f13f2be5dc42)

<img width="516" alt="CAD1" src="https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/1aa4391d-1b90-466d-acc4-aa58e77841c2">
<img width="762" alt="CAD3" src="https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/816fbc6c-1030-49b8-afb0-1c8032cbfa12">
<img width="740" alt="CAD2" src="https://github.com/Fernando1San/Manhattan-Project-for-NASA-Space-Apps/assets/113205429/342309a4-cc30-48ad-82b3-dcc47e919691">


#Technical Challenges
