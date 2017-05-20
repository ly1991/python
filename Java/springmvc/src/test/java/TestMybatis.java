import javax.annotation.Resource;

import com.ly.demo.service.UserService;
import junit.framework.TestCase;
import org.apache.log4j.Logger;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import static org.junit.Assert.assertEquals;

/**
 * Created by ly on 16/4/21.
 */
@RunWith(SpringJUnit4ClassRunner.class)        //表示继承了SpringJUnit4ClassRunner类
@ContextConfiguration(locations = {"classpath:spring-mybatis.xml"})
class TestMyBatis extends TestCase{
    private static Logger logger = Logger.getLogger(TestMyBatis.class);
    @Resource
    private UserService userService ;


    @Test
    public void test() {
//        User user = userService.getUserById(1);
        assertEquals(1,2+2);
    }
}
