#Problem 1

def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """

    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    #TODO 1: File processor with complete error handling

    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """

        file = None

        try:
            file = open(filename, "r")

        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None

        except PermissionError:
            print(f"No permission to access: {filename}")
            return None

        else:
            content = file.read()
            return content.upper()

        finally:
            if file:
                print(f"Closing {filename}")
                file.close()

    with open("exists.txt", "w") as f:
        f.write("hello world")

    test_files = ["exists.txt", "missing.txt", "/root/file"]

    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager

    class ResourceManager:

        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""

            print(f"Acquiring {self.name} resource...")

            if self.name == "BadResource":
                raise RuntimeError("Could not acquire resource")

            self.resource = True

        def release(self):
            """Release resource - must always happen."""

            if self.resource:
                print(f"Releasing {self.name} resource...")
                self.resource = None

        def use(self):
            """Use resource - only if acquired."""

            if not self.resource:
                raise RuntimeError("Resource not acquired")

            print(f"Using {self.name} resource")


    rm = ResourceManager("Database")

    try:
        rm.acquire()

    except RuntimeError as e:
        print(f"Error: {e}")

    else:
        rm.use()
        print("Resource used successfully")

    finally:
        rm.release()
        print("Cleanup complete")


practice_3_complete_pattern()


#problemn 2

def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """

    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions

    class GameError(Exception):
        """Base class for game exceptions."""
        pass
    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(
                f"Move {position} is invalid: {reason}"
            )

    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            self.winner = winner
            super().__init__(
                f"Game is already over. Winner: {winner}"
            )

    # TODO 2: Use custom exceptions

    class TicTacToe:

        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):

            if self.game_over:
                raise GameOverError("X")
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise InvalidMoveError(
                    (row, col),
                    "Position out of bounds"
                )

            if self.board[row][col] != ' ':
                raise InvalidMoveError(
                    (row, col),
                    "Position already taken"
                )

            self.board[row][col] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5)   # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")

        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")

        except GameOverError as e:
            print(f"🏁 Game over: {e}")


practice_2_custom_exceptions()


#problem 3


def practice_3_complete_system():
    """
    Build a complete error handling system
    """

    print("\n" + "=" * 50)
    print("EXERCISE 6: Complete Error Handler")
    print("=" * 50)

    class FileProcessor:

        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """

            file = None

            try:
                file = open(filename, "r")

            except FileNotFoundError:
                print(f"❌ File not found: {filename}")
                self.failed_files.append(filename)

            except PermissionError:
                print(f"❌ Permission denied: {filename}")
                self.failed_files.append(filename)

            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                self.failed_files.append(filename)

            else:
                content = file.read()

                print(f"✅ Successfully processed {filename}")
                print(f"   Characters: {len(content)}")

                self.processed_files.append(filename)

            finally:
                if file:
                    file.close()
                    print(f"   Closed {filename}")

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """

            import os

            try:
                for filename in os.listdir(directory):

                    full_path = os.path.join(directory, filename)

                    if os.path.isfile(full_path):
                        self.process_file(full_path)

            except Exception as e:
                print(f"Directory error: {e}")

        def get_report(self):
            """
            Get processing report.
            """

            return {
                "processed_count": len(self.processed_files),
                "failed_count": len(self.failed_files),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files
            }

    with open("valid.txt", "w") as f:
        f.write("This is a valid test file.\n")


    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()

    print("\nFinal Report")
    print("-" * 30)
    print(f"Processed: {report['processed_count']}")
    print(f"Failed: {report['failed_count']}")
    print(f"Processed Files: {report['processed_files']}")
    print(f"Failed Files: {report['failed_files']}")

practice_3_complete_system()
