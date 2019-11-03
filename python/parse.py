# encoding=utf-8
import os


def run(filename):
    # summary count of one file
    comment_count = 0
    blank_count = 0
    count = 0
    file = open(filename, errors='replace')
    print("filename {}".format(filename))
    flag = False
    for line in file.readlines():
        count += 1
        if not line.strip():
            blank_count += 1
            continue
        if line.strip().startswith("//"):
            comment_count += 1
        elif line.strip().startswith("/*"):
            comment_count += 1
            if line.find("*/") == -1:
                flag = True
        elif flag and line.strip().find("*/") != -1:
            comment_count += 1
            flag = False
        elif flag:
            comment_count += 1
    file.close()
    code_count = count - blank_count - comment_count
    return (code_count, blank_count, comment_count)


def main(root_dir, ext, depth):
    ret = {}

    def get_line_num(source, depth):
        depth -= 1
        if depth == -1:
            return
        if not os.path.exists(source):
            return
        if not os.path.isdir(source) and source[-len(ext):] == ext:
            ret[source] = run(source)
        else:
            for root, dirs, files in os.walk(source):
                for dir in dirs:
                    get_line_num(os.path.join(root, dir), depth)
                for file in files:
                    if file[-len(ext):] == ext:
                        ret[file] = run(os.path.join(root, file))
        return

    get_line_num(root_dir, depth)

    code_count = 0
    blank_count = 0
    comment_count = 0

    print(ret)

    for _, item in ret.items():
        code_count += item[0]
        blank_count += item[1]
        comment_count += item[2]
    print("files: {} \ncode_count: {} \nblank_count: {} \ncomment_count: {} ".format(len(ret), code_count, blank_count,
                                                                                     comment_count))


if __name__ == "__main__":
    main("./project/self/git_tool", '.java', -1)
