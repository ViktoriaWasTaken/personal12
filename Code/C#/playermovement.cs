public class PlayerMovement : MonoBehaviour
{
    void Start()
    {
        ball_Rigidbody.AddForce(transform.forward * 2500f);
    }

    void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.name == "Cylinder") {
            print("You lose!");
        }
    }
    // Speed at which the player moves
    public float speed = 5.0f;

    // Update is called once per frame
    void Update()
    {
        // Get input from the horizontal and vertical axes
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        // Use the input to move the player in the desired direction
        transform.position += new Vector3(horizontal, 0, vertical) * speed * Time.deltaTime;
    }
}