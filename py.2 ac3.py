from math import floor
qnt_channels = int(input())
channels = {}

for _ in range(0, qnt_channels):
    channel_data_input = input().split(';')
    channels[channel_data_input[0]] = {
        "subscribers": int(channel_data_input[1]),
        "monetization": float(channel_data_input[2]),
        "premium_content": channel_data_input[3]
    }

bonus_for_premium = float(input())
bonus_for_non_premium = float(input())


def calculate_bonus(channel_data):
    subscribers = channel_data["subscribers"]
    monetization = channel_data["monetization"]
    if channel_data["premium_content"] == "sim":
        return monetization + floor(subscribers/1000)*bonus_for_premium
    else:
        return monetization + floor(subscribers/1000)*bonus_for_non_premium


print("-----")
print("BÔNUS")
print("-----")

for channel, channel_data in channels.items():
    print("{}: R$ {:.2f}".format(channel, calculate_bonus(channel_data)))
