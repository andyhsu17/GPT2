from simpletransformers.conv_ai import ConvAIModel
#from py_imessage import imessage

andyiphone = "13032534350"

def main() -> None:
#    if not imessage.check_compatibility(andyiphone):
#        print("Not an iphone, quitting chatbot")

    train_args = {
            "overwrite_output_dir": True,
            "reprocess_input_data": True,
            "train_batch_size": 2
    }
    model = ConvAIModel("gpt", "gpt_personachat_cache", use_cuda=False, args=train_args)
    model.train_model()
    model.interact()

    # model = ConvAIModel("gpt2", "outputs")

def run():
    while(True):
        user_input = input()
        if (user_input == "q"):
            break
        elif(user_input == "\n"):
            continue
        response = bot.get_response(user_input)
        print(response)


if __name__ == '__main__':
    main()
