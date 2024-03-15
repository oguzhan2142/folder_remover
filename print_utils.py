def print_progress_bar(progress, total):
    progress = int(progress)
    total = int(total)
    bar_length = 50
    block = int(round(bar_length * progress / total))
    text = f"\rProgress: [{'#' * block}{'-' * (bar_length - block)}] {progress}/{total}"
    print(text, end="")
    if progress == total:
        print("")