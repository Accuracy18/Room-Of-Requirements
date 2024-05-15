#! /usr/bin/python3
import google.generativeai as genai, argparse, os # type: ignore

parser = argparse.ArgumentParser(description='Your program description')

parser.add_argument('-r', '--request', required=True)

args = parser.parse_args()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')
instruction = "Instructions: just give the code without text formatting, remove anything involving '''python''': "
response = model.generate_content(args.request)
print(response.text)
