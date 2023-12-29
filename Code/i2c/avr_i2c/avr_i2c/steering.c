/*
 * Styrmodul.c
 *
 * Created: 2023-11-07 13:04:22
 * Author : eliry213
 */ 

#include "steering.h"

#define F_CPU 1000000UL

#define set_bit(port, bit) (port) |= (1<<(bit))
#define clear_bit(port, bit) (port) &= ~(1<<(bit))
#define get_bit(port, bit) (port) & (1<<(bit))

#define LEFT_WHEEL_SPEED OCR1A
#define RIGHT_WHEEL_SPEED OCR1B

#define LEFT_DIR_PORT PORTB0
#define RIGHT_DIR_PORT PORTB1
#define LEFT_PWM_PORT PORTD4
#define RIGHT_PWM_PORT PORTD5

#define ROTATE_SPEED 40
#define ROTATE_DELAY 4800

volatile uint8_t current_speed;

/*
left direction = PORTA 0 (PB0/1) 5
right direction= PORTA 1 (PB1/2) 6
left wheel speed = OCR1A (PD5/19) 8
right wheel speed OCR1B  (PD4/18) 7
*/

void pwm_init() {
	DDRB |= 1<<LEFT_DIR_PORT | 1<<RIGHT_DIR_PORT; 
	DDRD |= 1<<LEFT_PWM_PORT | 1<<RIGHT_PWM_PORT;
	ICR1 = 255;
	TCCR1A |= (1 << COM1A1) | (1 << COM1B1) | (1 << WGM10);
	TCCR1B |= 1 << WGM31 | 1 << WGM21 | 1 << CS10;
}

// Sets the direction of both wheels
void set_direction(enum Direction dir){
	set_left_wheels(dir);
	set_right_wheels(dir);
}

// Rotates robot to the left
void rotate_left() {
	set_left_wheels(BACKWARD);
	set_right_wheels(FORWARD);
}

// Rotates robot to the right
void rotate_right() {
	set_right_wheels(BACKWARD);
	set_left_wheels(FORWARD);
}

// Sets direction of left wheel pair
void set_left_wheels(enum Direction dir) {
	if (dir == FORWARD) {
		set_bit(PORTB, LEFT_DIR_PORT);
	}
	else if (dir == BACKWARD) {
		clear_bit(PORTB, LEFT_DIR_PORT);
	}
	else {
		return;
	}
}

// Sets direction of right wheel pair
void set_right_wheels(enum Direction dir) {
	if (dir == FORWARD) {
		set_bit(PORTB, RIGHT_DIR_PORT);
	}
	else if (dir == BACKWARD) {
		clear_bit(PORTB, RIGHT_DIR_PORT);
	}
	else {
		return;
	}
}

// Sets speed of both wheels
void set_speed(uint8_t speed) {
	LEFT_WHEEL_SPEED = speed;
	RIGHT_WHEEL_SPEED = speed;
	current_speed = speed;
}

// Stops wheels by setting speed to 0
void stop() {
	set_speed(0);
}

// Turns robot to the right while driving
void turn_right() {
	RIGHT_WHEEL_SPEED = current_speed / 3;
	LEFT_WHEEL_SPEED = current_speed;
}

// Turns robot to the left while driving
void turn_left() {
	LEFT_WHEEL_SPEED = current_speed / 3;
	RIGHT_WHEEL_SPEED = current_speed;
}

void stop_turning() {
	set_speed(current_speed);
}

// Rotates robot 90 degrees to the left
void rotate_90_left() {
	set_speed(ROTATE_SPEED);
	rotate_left();
	_delay_ms(ROTATE_DELAY);
	stop();
}

// Rotates robot 90 degrees to the right
void rotate_90_right() {
	set_speed(ROTATE_SPEED);
	rotate_right();
	_delay_ms(ROTATE_DELAY);
	stop();
}