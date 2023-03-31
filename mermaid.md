


update                             
 - dump  
 - present                         
 - render                          
 - - draw_polygons                
 - - -  project_screen_coordinates
 - - -  frustrum_cull             
 - - -  project_in_screen_space   
 - - -  z_sort                    
 - - -  project_in_camera_space   
 - - -  normal_cull               
 - rotate                          
 - rotate                          
 - rotate        


 basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, and stepBefore.

:::mermaid
%%{ init: { 'flowchart': { 'curve': 'linear' } } }%%
graph TB
    classDef default fill:#222 outline:#000

    update[update] --> 
    
    event_processing --> update_state
    subgraph update_state
        state1[rotate1]
    end

    update_state --> render
    
    render
    subgraph render
        subgraph draw_polygons
            project_screen_coordinates -->
            frustrum_cull -->
            project_in_screen_space -->
            z_sort -->
            project_in_camera_space -->
            normal_cull
        end
    end


    render --> render_to_screen
    render_to_screen -->

    End(end)
:::


{root :{
    update:{
        event_processing:event_processing
        update_state:{
            rotate
        }
        render:{
            draw_polygons:{
            project_screen_coordinates
            frustrum_cull
            project_in_screen_space
            z_sort
            project_in_camera_space
            normal_cull
            }
        render_to_screen
        }
    }
}

                           