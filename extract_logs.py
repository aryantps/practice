import subprocess
import re


def extract_syslog():
    result = subprocess.run(["syslog"], capture_output=True)
    result = result.stdout.decode()

    for line in result.splitlines():
        try:
            if process_match(line) is not None:
                try:
                    log_string = "DATE : {}, PROCESS : {}, NOTICE :{}".format(
                        date_match(line), process_match(line), notice_match(line)
                    )
                    print(log_string)
                except AttributeError:
                    # print('lvl-2')
                    try:
                        print(
                            "DATE : {}, PROCESS : {}".format(
                                date_match(line), process_match(line)
                            )
                        )
                        print(" " * 30 + "└──  ERROR :", error_match(line))
                    except:
                        # print('lvl-3')
                        print(
                            "DATE : {}, PROCESS : {}".format(
                                date_match(line), process_match(line)
                            )
                        )
                        print(" " * 30 + "└──  WARNING :", warning_match(line))

        except:
            # print('lvl1')
            pass


process_match = lambda line : (re.search(r"Pro ([\w. ]*)",line)).group(1) if result else None
notice_match = lambda line : (re.search(r"e>: ([ \w:|]*)",line)).group(1) if result else None
warning_match = lambda line : (re.search(r"g>: ([ \w:=/.,\[\]()/]*)",line)).group(1) if result else None
date_match = lambda line : (re.search(r"(\w{3}[ \d:]+)",line)).group(1) if result else None
error_match = lambda line : (re.search(r"r>: ([ \"\"\w:=/.,()/\[\]]*)",line)).group(1) if result else None

extract_syslog()
