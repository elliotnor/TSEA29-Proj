
#ifndef ADCONVERTER_H_
#define ADCONVERTER_H_
#include <stdbool.h>
#include <avr/io.h>


void initADC(void);

bool is_ready(void);

void adc_start();

uint8_t adc_read(void);

#endif
