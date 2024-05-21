# there is a vulnerability. find it
def calculate_next_billing_date
    today = Date.today
    begin Date.new(today.year+1, today.month, today.day) rescue nil end
end