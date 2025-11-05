hour, minute = gets.chomp.split.map(&:to_i)
duration = gets.chomp.to_i

time_minute = duration % 60
minute = minute + time_minute
if minute >= 60
    minute -= 60
    hour = hour + 1
end

time_hour = duration / 60
hour = hour + time_hour
if hour >= 24
    hour = hour - 24
end
    
print "#{hour} #{minute}"