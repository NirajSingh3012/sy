def lru(page_references, num_frames):
    frame_order = []  # List to keep track of the order in which pages were referenced
    page_faults = 0  # Counter for page faults

    for page in page_references:
        if page not in frame_order:
            if len(frame_order) < num_frames:
                # If there's space in memory, add the page to the frame_order
                frame_order.append(page)
            else:
                # If the memory is full, remove the least recently used page
                # (the one at the front of the frame_order list)
                lru_page = frame_order.pop(0)
                print(f"Page {lru_page} removed from memory")

                # Add the new page to the frame_order
                frame_order.append(page)

            # Increment the page fault counter
            page_faults += 1
        else:
            # If the page is already in memory, move it to the most recently used position
            frame_order.remove(page)
            frame_order.append(page)

        print(f"Page {page}: Memory -> {frame_order}")

    return page_faults

if __name__ == "__main__":
    # Example usage:
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    num_frames = 3

    print("LRU Page Replacement Algorithm Simulation")
    print(f"Number of Frames in Memory: {num_frames}")
    print("\nPage Reference Sequence:")

    for page in pages:
        print(page, end=" ")

    print("\n\nSimulation Steps:")

    page_faults = lru(pages, num_frames)
    print(f"\nTotal page faults: {page_faults}")
