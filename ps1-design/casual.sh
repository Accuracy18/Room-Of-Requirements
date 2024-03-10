# Define colors for the prompt
BRIGHT_CYAN="\[\033[1;36m\]"
BRIGHT_GREEN="\[\033[1;32m\]"
BRIGHT_MAGENTA="\[\033[1;35m\]"
BRIGHT_RED="\[\033[1;31m\]"
BRIGHT_BLUE="\[\033[1;34m\]"
RESET="\[\033[0m\]"

# Function to get git branch (if in a git directory)
git_branch() {
    git branch 2>/dev/null | grep -e '^*' | sed 's/^* //'
}

ranger_prompt_segment() {
  if [[ "$RANGER_LEVEL" -gt 0 ]]; then
    echo "      $BRIGHT_RED ranger $RESET"
  fi
}

# PS1 prompt with multi-line sections
PS1="\n$BRIGHT_CYAN╭─$BRIGHT_GREEN\u$BRIGHT_CYAN$(echo -e '\xe2\x98\xA0')$BRIGHT_MAGENTA\h$BRIGHT_CYAN:$BRIGHT_MAGENTA\w$BRIGHT_CYAN\n"
PS1="$PS1$BRIGHT_CYAN╰─$BRIGHT_GREEN\$(git_branch)$RESET $(ranger_prompt_segment) \n"
PS1="$PS1$BRIGHT_CYAN╰─>$RESET "
export PS1
