#include <SFML/Graphics.hpp>
#include <iostream>

// Class for player paddle
class Player {
public:
    sf::RectangleShape paddle;
    float speed;

    Player(float width, float height) {
        paddle.setSize(sf::Vector2f(width, height));
        paddle.setFillColor(sf::Color::Green);
        paddle.setPosition(170, 260); // Paddle near bottom of 400x300 window
        speed = 0.3f;
    }

    void moveLeft() {
        if (paddle.getPosition().x > 0)
            paddle.move(-speed, 0);
    }

    void moveRight() {
        if (paddle.getPosition().x + paddle.getSize().x < 400)
            paddle.move(speed, 0);
    }
};

int main() {
    // Create a window of size 400x300
    sf::RenderWindow window(sf::VideoMode(400, 300), "Hit or Miss Ball");

    // Create a ball (circle) with radius 50
    sf::CircleShape ball(20);
    ball.setFillColor(sf::Color::White);
    
    // Initial position of the ball (starting near the center)
    ball.setPosition(100, 100);

    // Ball velocity (initially moving in both X and Y directions)
    sf::Vector2f velocity(0.2f, 0.2f); // X and Y velocities

    // Create player paddle
    Player player(80, 10);

    // Font and message
    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        std::cout << "Error loading font!\n";
        return -1;
    }

    sf::Text message("Press Space bar to continue", font, 20);
    message.setFillColor(sf::Color::Red);
    sf::FloatRect msgRect = message.getLocalBounds();
    message.setOrigin(msgRect.width / 2, msgRect.height / 2);
    message.setPosition(200, 150);

    bool gamePaused = false;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Handle keyboard input for paddle
        if (!gamePaused) {
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
                player.moveLeft();
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
                player.moveRight();
        }

        // Get the current position of the ball
        sf::Vector2f position = ball.getPosition();

        if (!gamePaused) {
            // Check for collision with the walls and bounce back
            if (position.x <= 0 || position.x + ball.getRadius() * 2 >= 400) {
                velocity.x = -velocity.x;  // Reverse direction in X axis
            }
            if (position.y <= 0) {
                velocity.y = -velocity.y;  // Reverse direction in Y axis
            }

            // Check for collision with paddle
            if (ball.getGlobalBounds().intersects(player.paddle.getGlobalBounds())) {
                velocity.y = -velocity.y;
            }

            // If ball misses the paddle, pause the game
            if (position.y + ball.getRadius() * 2 >= 300) {
                gamePaused = true;
            }

            // Move the ball by the velocity
            ball.move(velocity);
        } else {
            // Restart when Space is pressed
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space)) {
                ball.setPosition(100, 100);
                velocity = sf::Vector2f(0.2f, 0.2f);
                gamePaused = false;
            }
        }

        // Clear the screen
        window.clear();

        // Draw the ball
        window.draw(ball);

        // Draw the paddle
        window.draw(player.paddle);

        // Display message if paused
        if (gamePaused)
            window.draw(message);

        // Display the contents
        window.display();
    }

    return 0;
}
