#! /usr/bin/python3
import google.generativeai as genai, argparse, os, json # type: ignore

parser = argparse.ArgumentParser(description='Your program description')

parser.add_argument('-r', '--request', required=True)

args = parser.parse_args()

configs = {}
with open("/home/jojo/.config/micro/plug/AIplugin/config.json", "r") as file_x:
    configs = json.load(file_x)
    
genai.configure(api_key=configs["GOOGLE_API_KEY"])

model = genai.GenerativeModel(
    'gemini-2.0-flash',
    generation_config = {
        'max_output_tokens': 200,  # Adjust as needed
        'temperature': 0.4, # Adjust as needed
        'stop_sequences': ['# End of explanation']
    }
)
instruction = f"write a python method to: {args.request}"
response = model.generate_content(instruction)
print(response.text)
