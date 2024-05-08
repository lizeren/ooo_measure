# Define the compiler
CC=gcc

# Define any compile-time flags
CFLAGS=-O0

# ANSI color codes
GREEN=\033[0;32m
BLUE=\033[0;34m
RED=\033[0;31m
NC=\033[0m # No Color

# Default target: hint
all:
	@echo "Specify a target: q1, q2, q3, q4, run1, run2, etc."

# Specific compilation rules
#Index:value​, Load after IF
q1: Out_of_order1.c
	@$(CC) $(CFLAGS) $< -o execute1
	@printf "$(GREEN)Compilation complete: execute1$(NC)\n"

q2: Out_of_order2.c
	@$(CC) $(CFLAGS) $< -o execute2
	@printf "$(GREEN)Compilation complete: execute2$(NC)\n"

q3: Out_of_order3.c
	@$(CC) $(CFLAGS) $< -o execute3
	@printf "$(GREEN)Compilation complete: execute3$(NC)\n"

q4: Out_of_order4.c
	@$(CC) $(CFLAGS) $< -o execute4
	@printf "$(GREEN)Compilation complete: execute4$(NC)\n"

# Execute targets: Specific rules for running executables
run1 run2 run3 run4: run%:
	@if [ -f execute$* ]; then \
		./execute$*; \
		printf "$(BLUE)Execution complete: execute$*$(NC)\n"; \
	else \
		printf "$(RED)Error: No executable found for run$*. Specify a valid target, e.g., run1, run2, etc.$(NC)\n"; \
	fi

# Fallback for general 'run' without a specific number
run:
	@printf "$(RED)Error: Please specify a valid target number for execution, e.g., make run1, make run2, etc.$(NC)\n"

# Clean target: remove all executables
clean:
	@rm -f execute1 execute2 execute3 execute4
	@printf "$(GREEN)Cleaned$(NC)\n"
