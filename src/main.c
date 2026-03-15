/*============================================================
Project : ESP32-S3 N8R2 2.8" SPI TFT Display Stack
Author  : Shantanu Kumar
GitHub  : https://github.com/shantanuk47

Date    : 
File    : main.c
Purpose : System boot validation
============================================================*/

#include <stdio.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "version.h"

void app_main(void)
{
    printf("\n");
    printf("=====================================\n");
    printf(" ESP32-S3 Display Stack Boot\n");
    printf(" Firmware Version : %s\n", FW_VERSION);
    printf(" Build Date       : %s\n", FW_BUILD_DATE);
    printf(" Build Time       : %s\n", FW_BUILD_TIME);
    printf("=====================================\n\n");

    while (1)
    {
        printf("System running...\n");
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}